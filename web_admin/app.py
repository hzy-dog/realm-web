from flask import Flask, render_template, request, redirect, session, url_for
import yaml
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 可修改
CONFIG_PATH = '/etc/realm/realm_config.yaml'
AUTH_CONFIG = 'web_admin/config.yaml'

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config, f)

def load_auth():
    with open(AUTH_CONFIG, 'r') as f:
        return yaml.safe_load(f)

@app.before_request
def require_login():
    if request.endpoint not in ['login', 'static'] and not session.get('logged_in'):
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    cfg = load_auth()['auth']
    if request.method == 'POST':
        if request.form['username'] == cfg['username'] and request.form['password'] == cfg['password']:
            session['logged_in'] = True
            return redirect('/')
        return 'Login Failed'
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    config = load_config()
    if request.method == 'POST':
        listen_port = int(request.form['listen_port'])
        remote_host = request.form['remote_host']
        remote_port = int(request.form['remote_port'])
        proto = request.form['protocol']
        tag = f'{proto}_{listen_port}'

        inb = {
            'type': proto,
            'listen': f'0.0.0.0:{listen_port}',
            'tag': f'in_{tag}'
        }
        if 'enable_tls' in request.form:
            inb['tls'] = {
                'cert': request.form['cert'],
                'key': request.form['key']
            }

        outb = {
            'type': proto,
            'tag': f'in_{tag}',
            'address': remote_host,
            'port': remote_port
        }

        config['inbounds'].append(inb)
        config['outbounds'].append(outb)
        save_config(config)
        os.system('systemctl restart realm')
        return redirect('/')
    return render_template('index.html', config=config)

@app.route('/delete/<tag>')
def delete(tag):
    config = load_config()
    config['inbounds'] = [x for x in config['inbounds'] if x.get('tag') != tag]
    config['outbounds'] = [x for x in config['outbounds'] if x.get('tag') != tag]
    save_config(config)
    os.system('systemctl restart realm')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7655)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    auth_config = load_auth()
    config = load_config()

    if request.method == 'POST':
        auth_config['auth']['username'] = request.form['username']
        auth_config['auth']['password'] = request.form['password']
        with open(AUTH_CONFIG, 'w') as f:
            yaml.dump(auth_config, f)

        # 记录默认 TLS 证书路径（非必须）
        with open('web_admin/default_tls.yaml', 'w') as f:
            yaml.dump({
                'cert': request.form['cert'],
                'key': request.form['key']
            }, f)

        return redirect('/')
    return render_template('settings.html')
