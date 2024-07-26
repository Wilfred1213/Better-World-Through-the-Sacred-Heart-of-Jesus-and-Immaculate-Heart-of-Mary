# # myapp/middleware.py

# from simple_analytics.tracker import track_page_view  # Hypothetical function

# class CustomAnalyticsMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Code to execute for each request before the view (and later middleware) are called.
#         response = self.get_response(request)

#         # Code to execute for each request/response after the view is called.
#         track_page_view(request)  # Hypothetical function call to track the page view

#         return response
