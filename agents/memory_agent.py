import os
import json
import hashlib


class MemoryAgent:

    def __init__(self):
        self.domain_db = "domains_memory.json"
        self.query_db = "queries_memory.json"
        self.lead_db = "leads_memory.json"

        self.domains = self._load(self.domain_db)
        self.queries = self._load(self.query_db)
        self.leads = self._load(self.lead_db)

    def _load(self, file):
        if os.path.exists(file):
            with open(file, "r") as f:
                return json.load(f)
        return {}

    def _save(self, file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=2)

    #################################################
    # DOMAIN MEMORY
    #################################################

    def exists_domain(self, domain):
        return domain.lower() in self.domains

    def save_domain(self, domain):
        self.domains[domain.lower()] = True
        self._save(self.domain_db, self.domains)

    #################################################
    # QUERY MEMORY
    #################################################

    def exists_query(self, query):
        return query.lower() in self.queries

    def save_query(self, query):
        self.queries[query.lower()] = True
        self._save(self.query_db, self.queries)

    #################################################
    # LEAD MEMORY
    #################################################

    def fingerprint(self, lead):

        text = (
            str(lead.get("company_name", "")) +
            str(lead.get("company_website", "")) +
            str(lead.get("phone_number", "")) +
            str(lead.get("linkedin", ""))
        )

        return hashlib.md5(
            text.lower().encode()
        ).hexdigest()

    def exists(self, lead):
        fp = self.fingerprint(lead)
        return fp in self.leads

    def save(self, lead):
        fp = self.fingerprint(lead)

        if fp not in self.leads:
            self.leads[fp] = True
            self._save(
                self.lead_db,
                self.leads
            )