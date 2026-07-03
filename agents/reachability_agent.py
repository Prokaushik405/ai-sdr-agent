class ReachabilityAgent:

    def check(self, lead):

        emails = lead.get("emails", [])
        phone = lead.get("phone_number", "")
        whatsapp = lead.get("whatsapp_number", "")

        linkedin = lead.get("linkedin", "")
        instagram = lead.get("instagram", "")
        twitter = lead.get("twitter", "")
        youtube = lead.get("youtube", "")

        reachable = False
        channel = None

        # Email outreach
        if emails and emails != "NA":
            reachable = True
            channel = "email"

        # Phone outreach
        elif phone not in ["", "NA", None]:
            reachable = True
            channel = "phone"

        # Whatsapp outreach
        elif whatsapp not in ["", "NA", None]:
            reachable = True
            channel = "whatsapp"

        # DM outreach
        elif linkedin not in ["", "NA", None]:
            reachable = True
            channel = "linkedin"

        elif instagram not in ["", "NA", None]:
            reachable = True
            channel = "instagram"

        elif twitter not in ["", "NA", None]:
            reachable = True
            channel = "twitter"

        elif youtube not in ["", "NA", None]:
            reachable = True
            channel = "youtube"

        lead["reachable"] = reachable
        lead["outreach_channel"] = channel
        print()
        print("EMAILS:", emails)
        print("PHONE:", phone)
        print("WHATSAPP:", whatsapp)
        print("LINKEDIN:", linkedin)
        print("INSTAGRAM:", instagram)
        print("TWITTER:", twitter)
        print("YOUTUBE:", youtube)
        print("REACHABLE:", reachable)
        print("CHANNEL:", channel)
        print()
        return lead