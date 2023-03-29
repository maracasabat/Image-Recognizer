def theme(request):
    if 'is_dark_theme' in request.session:
        return {'is_dark_theme': request.session['is_dark_theme']}
    else:
        return {'is_dark_theme': False}