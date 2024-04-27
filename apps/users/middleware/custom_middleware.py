class SessionDurationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Apply custom session duration only if user is authenticated
        if request.user.is_authenticated:
            # Set session duration based on user
            session_expiry = request.user.session_duration  # get database duration
            request.session.set_expiry(session_expiry)  # sets the session duration

        return response
