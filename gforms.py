import requests

class Form ():

    def __init__ (self, form_id, fields):
        self.prefix = 'https://docs.google.com/forms/d/'
        self.id = form_id
        self.field_url = '/formResponse?'
        self.fields = fields
        self.suffix = '&submit=Submit'
        self.fields_string = self.fields_to_string()
        self.post_url = self.prefix + self.id + self.field_url + self.fields_string + self.suffix

    def fields_to_string(self):
        field_strings = []
        for field, value in self.fields.items():
            field_string = 'entry.%s=%s' % (field, value)
            field_strings.append(field_string)
        return "&".join(field_strings)

    def build_url(self):
        url = self.prefix + self.id 

    def post(self):
        r = requests.post(self.post_url)
        print "Posting: %s - %d" % (self.post_url, r.status_code)


# fields and values (get field id by insepecting element on form)
fields = {
    '1111111111':'value0', # form_field_id: value
    '2222222222':'value1',
    '3333333333':'value2'
}

# inti form
cool_form = Form('1VQ8CYSuxyb01jKdp6zZGxtWct4RWdqjzC7_2-VddaIA', fields).post()

# post with requests
cool_form.post()
