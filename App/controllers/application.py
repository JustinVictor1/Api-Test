from App.models.job import Job
from App.models.applicant import Applicant
from App.models.application import Application
from App.database import db


def create_application(job_id, applicant_id):
    job = Job.query.get(job_id)
    applicant = Applicant.query.get(applicant_id)

    # Check if the job or applicant is None
    if not job:
        print(f"Job with ID {job_id} not found.")
        return {"error": f"Job with ID {job_id} not found"}, 404

    if not applicant:
        print(f"Applicant with ID {applicant_id} not found.")
        return {"error": f"Applicant with ID {applicant_id} not found"}, 404

    application = Application(job_id=job.job_id, applicant_id=applicant.applicant_id)
    db.session.add(application)
    db.session.commit()
    print(f"Application of '{applicant.applicant_id}' created for job {job.job_id}")
    return {"message": f"Application created for job {job_id}"}, 201


def get_all_applications():
    return Application.query.all()


def get_all_applications_json():
    applications = Application.query.all()
    if not applications:
        return []
    applications = [application.view_application_details() for application in applications]
    return applications
