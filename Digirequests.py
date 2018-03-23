class Digirequests:

    def __init__(self, title):
        timestamp, email, title, division, submitter, collection, scope, size, rationale, time, rights_online, rights_content, processing, metadata_description, metadata_catalog, metadata_issues, imaging_location, imaging_special, condition, date_range, ref_effort_score, ref_effort_notes, reg_effort_score, reg_effort_notes, cons_effort_score, cons_effort_notes, proc_effort_score, proc_effort_notes, meta_effort_score, meta_effort_notes, rights_effort_score, rights_effort_notes, access_effort_score, access_effort_notes = Digirequests.get_request_data(title)
        self.timestamp = timestamp
        self.email = email
        self.title = title
        self.division = division
        self.submitter = submitter
        self.collection = collection
        self.scope = scope
        self.size = size
        self.rationale = rationale
        self.time = time
        self.rights_online = rights_online
        self.rights_content = rights_content
        self.processing = processing
        self.metadata_description = metadata_description
        self.metadata_catalog = metadata_catalog
        self.metadata_issues = metadata_issues
        self.imaging_location = imaging_location
        self.imaging_special = imaging_special
        self.condition = condition
        self.date_range = date_range
        if not ref_effort_score:
            self.ref_effort_score = 'TBD'
        else:
            self.ref_effort_score = ref_effort_score
        self.ref_effort_notes = ref_effort_notes
        if not reg_effort_score:
            self.reg_effort_score = 'TBD'
        else:
            self.reg_effort_score = reg_effort_score
        self.reg_effort_notes = reg_effort_notes
        if not cons_effort_score:
            self.cons_effort_score = 'TBD'
        else:
            self.cons_effort_score = cons_effort_score
        self.cons_effort_notes = cons_effort_notes
        if not proc_effort_score:
            self.proc_effort_score = 'TBD'
        else:
            self.proc_effort_score = proc_effort_score
        self.proc_effort_notes = proc_effort_notes
        if not meta_effort_score:
            self.meta_effort_score = 'TBD'
        else:
            self.meta_effort_score = meta_effort_score
        self.meta_effort_notes = meta_effort_notes
        if not rights_effort_score:
            self.rights_effort_score = 'TBD'
        else:
            self.rights_effort_score = rights_effort_score
        self.rights_effort_notes = rights_effort_notes
        if not access_effort_score:
            self.access_effort_score = 'TBD'
        else:
            self.access_effort_score = access_effort_score
        self.access_effort_notes = access_effort_notes
        if str(5) in ref_effort_score:
            self.ref_effort_color = 'bg-danger'
            self.ref_effort_text = 'text-white'
        elif str(4) in ref_effort_score:
            self.ref_effort_color = 'bg-warning'
            self.ref_effort_text = 'text-black'
        elif str(3) in ref_effort_score:
            self.ref_effort_color = 'bg-primary'
            self.ref_effort_text = 'text-white'
        elif str(2) in ref_effort_score:
            self.ref_effort_color = 'bg-info'
            self.ref_effort_text = 'text-white'
        elif str(1) in ref_effort_score:
            self.ref_effort_color = 'bg-success'
            self.ref_effort_text = 'text-white'
        else:
            self.ref_effort_color = 'bg-light'
            self.ref_effort_text = 'text-black'
        if str(5) in reg_effort_score:
            self.reg_effort_color = 'bg-danger'
            self.reg_effort_text = 'text-white'
        elif str(4) in reg_effort_score:
            self.reg_effort_color = 'bg-warning'
            self.reg_effort_text = 'text-black'
        elif str(3) in reg_effort_score:
            self.reg_effort_color = 'bg-primary'
            self.reg_effort_text = 'text-white'
        elif str(2) in reg_effort_score:
            self.reg_effort_color = 'bg-info'
            self.reg_effort_text = 'text-white'
        elif str(1) in reg_effort_score:
            self.reg_effort_color = 'bg-success'
            self.reg_effort_text = 'text-white'
        else:
            self.reg_effort_color = 'bg-light'
            self.reg_effort_text = 'text-black'
        if str(5) in cons_effort_score:
            self.cons_effort_color = 'bg-danger'
            self.cons_effort_text = 'text-white'
        elif str(4) in cons_effort_score:
            self.cons_effort_color = 'bg-warning'
            self.cons_effort_text = 'text-black'
        elif str(3) in cons_effort_score:
            self.cons_effort_color = 'bg-primary'
            self.cons_effort_text = 'text-white'
        elif str(2) in cons_effort_score:
            self.cons_effort_color = 'bg-info'
            self.cons_effort_text = 'text-white'
        elif str(1) in cons_effort_score:
            self.cons_effort_color = 'bg-success'
            self.cons_effort_text = 'text-white'
        else:
            self.cons_effort_color = 'bg-light'
            self.cons_effort_text = 'text-black'
        if str(5) in proc_effort_score:
            self.proc_effort_color = 'bg-danger'
            self.proc_effort_text = 'text-white'
        elif str(4) in proc_effort_score:
            self.proc_effort_color = 'bg-warning'
            self.proc_effort_text = 'text-black'
        elif str(3) in proc_effort_score:
            self.proc_effort_color = 'bg-primary'
            self.proc_effort_text = 'text-white'
        elif str(2) in proc_effort_score:
            self.proc_effort_color = 'bg-info'
            self.proc_effort_text = 'text-white'
        elif str(1) in proc_effort_score:
            self.proc_effort_color = 'bg-success'
            self.proc_effort_text = 'text-white'
        else:
            self.proc_effort_color = 'bg-light'
            self.proc_effort_text = 'text-black'
        if str(5) in meta_effort_score:
            self.meta_effort_color = 'bg-danger'
            self.meta_effort_text = 'text-white'
        elif str(4) in meta_effort_score:
            self.meta_effort_color = 'bg-warning'
            self.meta_effort_text = 'text-black'
        elif str(3) in meta_effort_score:
            self.meta_effort_color = 'bg-primary'
            self.meta_effort_text = 'text-white'
        elif str(2) in meta_effort_score:
            self.meta_effort_color = 'bg-info'
            self.meta_effort_text = 'text-white'
        elif str(1) in meta_effort_score:
            self.meta_effort_color = 'bg-success'
            self.meta_effort_text = 'text-white'
        else:
            self.meta_effort_color = 'bg-light'
            self.meta_effort_text = 'text-black'
        if str(5) in rights_effort_score:
            self.rights_effort_color = 'bg-danger'
            self.rights_effort_text = 'text-white'
        elif str(4) in rights_effort_score:
            self.rights_effort_color = 'bg-warning'
            self.rights_effort_text = 'text-black'
        elif str(3) in rights_effort_score:
            self.rights_effort_color = 'bg-primary'
            self.rights_effort_text = 'text-white'
        elif str(2) in rights_effort_score:
            self.rights_effort_color = 'bg-info'
            self.rights_effort_text = 'text-white'
        elif str(1) in rights_effort_score:
            self.rights_effort_color = 'bg-success'
            self.rights_effort_text = 'text-white'
        else:
            self.rights_effort_color = 'bg-light'
            self.rights_effort_text = 'text-black'
        if str(5) in access_effort_score:
            self.access_effort_color = 'bg-danger'
            self.access_effort_text = 'text-white'
        elif str(4) in access_effort_score:
            self.access_effort_color = 'bg-warning'
            self.access_effort_text = 'text-black'
        elif str(3) in access_effort_score:
            self.access_effort_color = 'bg-primary'
            self.access_effort_text = 'text-white'
        elif str(2) in access_effort_score:
            self.access_effort_color = 'bg-info'
            self.access_effort_text = 'text-white'
        elif str(1) in access_effort_score:
            self.access_effort_color = 'bg-success'
            self.access_effort_text = 'text-white'
        else:
            self.access_effort_color = 'bg-light'
            self.access_effort_text = 'text-black'
    
    def get_request_data(title):
        import csv
        import requests
        import io

        r = requests.get('https://docs.google.com/spreadsheets/d/1BLvFt9l6ex6Gdv4Vx1WPuwXhDH0qlVoE1cbhiAas5Po/export?format=csv') 

        sio = io.StringIO( r.text, newline=None)
        reader = csv.reader(sio, dialect=csv.excel)

        for row in reader:
            if row[2] == title:
                timestamp = row[0]
                email = row[1]
                title = row[2]
                division = row[3]
                submitter = row[4]
                collection = row[5]
                scope = row[6]
                size = row[7]
                rationale = row[8]
                time = row[9]
                rights_online = row[10]
                rights_content = row[11]
                processing = row[12]
                metadata_description = row[13]
                metadata_catalog = row[14]
                metadata_issues = row[15]
                imaging_location = row[16]
                imaging_special = row[17]
                condition = row[18]
                date_range = row[19]
                ref_effort_score = row[22]
                ref_effort_notes = row[23]
                reg_effort_score = row[24]
                reg_effort_notes = row[25]
                cons_effort_score = row[26]
                cons_effort_notes = row[27]
                proc_effort_score = row[28]
                proc_effort_notes = row[29]
                meta_effort_score = row[30]
                meta_effort_notes = row[31]
                rights_effort_score = row[32]
                rights_effort_notes = row[33]
                access_effort_score = row[34]
                access_effort_notes = row[35]
                return timestamp, email, title, division, submitter, collection, scope, size, rationale, time, rights_online, rights_content, processing, metadata_description, metadata_catalog, metadata_issues, imaging_location, imaging_special, condition, date_range, ref_effort_score, ref_effort_notes, reg_effort_score, reg_effort_notes, cons_effort_score, cons_effort_notes, proc_effort_score, proc_effort_notes, meta_effort_score, meta_effort_notes, rights_effort_score, rights_effort_notes, access_effort_score, access_effort_notes


def main():

    import sys

    title = sys.argv[1]
    obj = Digirequests(title)
    print(obj.ref_effort_notes)


    import jinja2

    env = jinja2.Environment()
    env.loader = jinja2.FileSystemLoader('test_templates')

    template = env.get_template('request_template.html')

    completed_page = template.render(request=obj)

    wfh = open(title + '.html', 'w')
    wfh.write(completed_page)
    wfh.close()

if __name__ == '__main__':
    main()


