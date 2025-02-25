import time
import logging
from django.views.generic import View
from django.http import JsonResponse

logger = logging.getLogger("django")

class SampleView(View):
    def get(self, request):
        if not request.session.session_key:
            request.session.create() 
        session_key = request.session.session_key
        logger.info(f"Start: {session_key}")
        for i in range(3):
            logger.info(f"Process {i}")
            time.sleep(2)
        logger.info(f"Finish: {session_key}")
        return JsonResponse({"test": "ok"}, status=200)
