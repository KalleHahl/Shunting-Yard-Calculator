from invoke import task

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html', pty=True)

@task
def pylint(ctx):
    ctx.run('pylint src', pty=True)

@task
def pytest(ctx):
    ctx.run('pytest src', pty=True)
