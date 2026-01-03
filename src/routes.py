"""
Navigator Routes
HearthMind LLC
"""

from flask import Blueprint, render_template, current_app, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/benefits')
def benefits():
    benefits_data = current_app.config.get('BENEFITS', {})
    return render_template('benefits.html', benefits=benefits_data)

@bp.route('/resources')
def resources():
    resources_data = current_app.config.get('RESOURCES', {})
    local_data = current_app.config.get('LOCAL_RESOURCES', {})
    
    # Get selected state and city from query params (set by JS)
    state = request.args.get('state', '')
    city = request.args.get('city', '')
    
    # Get local resources for selected location
    local_resources = None
    if state and city:
        state_data = local_data.get(state, {})
        cities = state_data.get('cities', {})
        local_resources = cities.get(city, {})
        if local_resources:
            local_resources['state_name'] = state_data.get('name', state)
            local_resources['city_name'] = local_resources.get('name', city)
    
    return render_template('resources.html', 
                         resources=resources_data, 
                         local_resources=local_resources,
                         local_data=local_data,
                         selected_state=state,
                         selected_city=city)

@bp.route('/checklist')
def checklist():
    return render_template('checklist.html')

@bp.route('/timeline')
def timeline():
    return render_template('timeline.html')
