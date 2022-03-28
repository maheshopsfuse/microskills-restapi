from random import randint
from flask_restplus import Resource
from app.main.model.registration import Users
from app.main.utils.controller_dto.registration_dto import RegistrationDto
from twilio.rest import Client
from datetime import datetime

api = RegistrationDto.api


@api.route("api/phone/<string:type>/<string:phone>/<string:country>")
class Registration(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.account_sid = "ACf46dc60f7a01d43763530ca88f3b31c5"
        self.auth_token = "123f37b4df81be6c57e83cded5a848fa"
        self.client = Client(self.account_sid, self.auth_token)

    def get(self, type, phone, country):
        user = Users("Mahesh", "Nagmal", phone_number=phone)
        date_time = datetime.now().isoformat()
        phone_number = country + phone
        otp = self.genrateOTP()
        """if type == "call":
            self.sendOTPCall(otp, phone_number)
        else:
            self.sendOTP(otp, phone_number)"""
        print(type)
        print(phone_number)
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "opt": otp,
            "otp_sent_at": date_time
        }

    def post(self, type, phone, country):
        return {
            "first_name": "Mahesh",
            "last_name": "Nagmal"
        }

    def sendOTPSMS(self, otp, phone_number):
        message = self.client.messages \
            .create(
                body="Your OTP is {}".format(otp),
                from_='+15597808935',
                to=phone_number
            )
        print(message.sid)

    def sendOTPCall(self, otp, phone_number):
        call = self.client.calls.create(
            twiml=f"<Response><Say voice='alice'>Your one-time password is {otp}</Say><Pause length='1'/><Say>Your one-time password is {otp}</Say><Pause length='1'/><Say>Goodbye</Say></Response>",
            from_='+15597808935', to=phone_number
        )

    def genrateOTP(self):
        return randint(100000, 999999)
