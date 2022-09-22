'''
Given an array of count-paired domains cpdomains, 
return an array of the count-paired domains of each subdomain in the input. 
You may return the answer in any order.
'''
def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        final_visits = {}
        res = []
        for domain in cpdomains:
            count, dom = domain.split(" ")
            individual_subdomains = dom.split(".")
            top_level_domain = individual_subdomains[-1]
            final_visits[top_level_domain] = final_visits.get(top_level_domain,0) + int(count)
            while len(individual_subdomains) > 1:
                outer = individual_subdomains.pop()
                inner = individual_subdomains.pop()
                new_sub = f"{inner}.{outer}"
                final_visits[new_sub] = final_visits.get(new_sub,0) + int(count)
                individual_subdomains.append(new_sub)
        for k,v in final_visits.items():
            res.append(f"{v} {k}")
        return res