class HelloMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Hello, Middleware!")
        response = self.get_response(request)
        return response