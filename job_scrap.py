from indeed import get_jobs as get_indeed_jobs
# from wanted import get_jobs_wanted
from sof import get_jobs as get_sof_jobs
from toCsv import save_to_file as save


def scrap(keyword):
    indeed_jobs = get_indeed_jobs(keyword)
    sof_jobs = get_sof_jobs(keyword)
    # jobs = { "indeed": indeed_jobs, "sof": sof_jobs}
    jobs = indeed_jobs + sof_jobs
    # save(jobs)
    return jobs
