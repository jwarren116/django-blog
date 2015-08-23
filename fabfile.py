from fabric.api import run, local, get, cd, settings


def fetch_logs():
    logs_dir = "~/logs/jwarren.co/http/*.log"
    get(remote_path=logs_dir)


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    with settings(warn_only=True):
        commit()
    push()


def deploy():
    app_dir = "~/jwarren.co/"
    with cd(app_dir):
        run("git pull origin master")
        run("touch tmp/restart.txt")
