class Lead:

    def __init__(
        self,
        company_name="",
        founder_name="",
        founder_title="",
        website="",
        email="",
        phone="",
        whatsapp="",
        linkedin="",
        twitter="",
        instagram="",
        industry="",
        content_activity="",
        clipping_score=0,
        outreach_angle=""
    ):
        self.company_name = company_name
        self.founder_name = founder_name
        self.founder_title = founder_title
        self.website = website
        self.email = email
        self.phone = phone
        self.whatsapp = whatsapp
        self.linkedin = linkedin
        self.twitter = twitter
        self.instagram = instagram
        self.industry = industry
        self.content_activity = content_activity
        self.clipping_score = clipping_score
        self.outreach_angle = outreach_angle

    def to_dict(self):
        return self.__dict__