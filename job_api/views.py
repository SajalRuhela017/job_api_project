from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from .models import Job

@csrf_exempt
@require_POST
def add_job(request):
    job_id = request.GET.get('jobid', request.POST.get('jobid'))
    job_value = request.GET.get('jobValue', request.POST.get('jobValue'))
    
    # Create and save the job entity
    job = Job(job_id=job_id, job_value=job_value)
    job.save()
    
    return JsonResponse({'stat': 'ok'})

@require_GET
def get_jobs(request):
    start_value = request.GET.get('jobValue')
    if start_value is not None:
        jobs = Job.objects.filter(job_value__gte=start_value).order_by('job_value')
    else:
        jobs = Job.objects.all().order_by('job_value')
    
    job_list = [[job.job_id, job.job_value] for job in jobs]
    return JsonResponse(job_list, safe=False)

@csrf_exempt
@require_POST
def remove_job(request):
    job_id = request.GET.get('jobid', request.POST.get('jobid'))
    
    try:
        job = Job.objects.get(job_id=job_id)
        job.delete()
        return JsonResponse({'stat': 'ok'})
    except Job.DoesNotExist:
        return JsonResponse({'stat': 'Job not found'}, status=404)
