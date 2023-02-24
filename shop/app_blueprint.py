from quart import Quart, redirect, url_for, render_template, request, Blueprint, abort
from jinja2 import TemplateNotFound

app_blueprint = Blueprint('shop', __name__, template_folder='templates', static_folder='static')


@app_blueprint.route('/', defaults={'page': 'index.html'})
@app_blueprint.route('/<page>')
async def show(page):
    try:
        return await render_template('shop/%s' % (page))
    #except TemplateNotFound:
    #    abort(404)
    except Exception as e:
        raise e
