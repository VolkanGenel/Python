from django.core.mail import send_mail
from django.conf import settings

def send_email(passenger_email, reservation):
    subject = f"Reservation Confirmation: {reservation.reservation_code}"
    message = f"""
    Dear {reservation.passenger_name},
    
    Your Reservation {reservation.flight.flight_number} from {reservation.flight.departure}
    to {reservation.flight.destination} at {reservation.flight.departure_time} is approved!
    Please don't be late!
    
    KEEP THIS CODE!
    Reservation Code: {reservation.reservation_code}
    Created At: {reservation.created_at.strftime('%d-%m-%Y %H:%M:%S')}
    
    Best regards,
    Volkan Genel
    """
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, [passenger_email], fail_silently=False)