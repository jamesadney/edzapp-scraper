import re
from collections import defaultdict
import mechanize
from bs4 import BeautifulSoup


SHOWALL_BTN = 'ctl00$btnAllJobs'
SELECT_STATES_BTN = 'ctl00$VisibilityRegionSelector$rptChildren$ctl00$btnChild'
SEARCH_BTN = 'ctl00$btnSubmit'

SELECT_REGIONS = "ctl00$VisibilityRegionSelector$lstRegions"
REGIONS = {
    'US': '6',
    'INT': '281',
}

SELECT_STATES = SELECT_REGIONS
STATES = {
    'ARIZONA': '9',
    'CALIFORNIA': '10',
    'COLORADO': '11',
    'FLORIDA': '15',
    'GEORGIA': '16',
    'IDAHO': '19',
    'INDIANA': '21',
    'MINNESOTA': '29',
    'MONTANA': '33',
    'NORTHDAKOTA': '35',
    'NEVADA': '40',
    'NEWYORK': '41',
    'OHIO': '42',
    'OKLAHOMA': '43',
    'OREGON': '44',
    'PENNSYLVANIA': '45',
    'TENNESSEE': '50',
    'TEXAS': '51',
    'WASHINGTON': '56',
    'WISCONSIN': '57',
    'WYOMING': '59',
    'DOHAQATAR': '21292',
}

SCHEDS = {
    "FULLTIME": "ctl00$chkTypeID$0",
    "PARTTIME": "ctl00$chkTypeID$1",
    "TEMPORARY": "ctl00$chkTypeID$2",
    "SUBSTITUTE": "ctl00$chkTypeID$3",
    "OTHER": "ctl00$chkTypeID$4",
    "UNSPECIFIED": "ctl00$chkTypeID$5",
    "LIMITED": "ctl00$chkTypeID$6",
    "PERMANENT": "ctl00$chkTypeID$7",
}

SELECT_SUBJECTS = "ctl00$lstSubjectID"
SUBS = {
    'ACCOUNTING': '1599',
    'ADMINISTRATION': '506',
    'ADVERTISING': '3010',
    'AFTERSCHOOLACTIVITIESDIRECTOR': '535',
    'AGRICULTURE': '80',
    'ALTERNATIVEEDUCATION': '3083',
    'ARCHITECTURE': '2328',
    'ARTVISUALEDUCATION': '14',
    'ASSISTANTVICEPRINCIPAL': '192',
    'ASSISTANTPRINCIPALELEMENTARYSCHOOL': '2215',
    'ASSISTANTPRINCIPALHIGHSCHOOL': '2066',
    'ASSISTANTPRINCIPALMIDDLESCHOOL': '1695',
    'ASSISTANTSUPERINTENDENT': '1060',
    'AUDIOLOGIST': '132',
    'AVIDTUTOR': '547',
    'BILINGUALEDUCATION': '133',
    'BUSINESSEDUCATION': '16',
    'BUSINESSMANAGER': '164',
    'CHILDDEVELOPMENT': '1402',
    'COACH': '604',
    'COLLEGECOUNSELOR': '10674',
    'COMMUNICATIONS': '1511',
    'COMPUTERSCIENCEEDUCATION': '17',
    'COUNSELOR': '7',
    'CRIMINALJUSTICE': '126',
    'CURRICULUMDIRECTOR': '165',
    'CUSTODIAL': '6866',
    'DANCEEDUCATION': '134',
    'DAYCARE': '701',
    'DRIVEREDUCATIONTRAFFICSAFETY': '34',
    'EARLYCHILDHOODEDUCATIONMULTIPLESUBJECTS': '48',
    'ECEELE': '586',
    'EDUCATIONALASSISTANT': '352',
    'ELEMENTARYEDUCATIONMULTIPLESUBJECTS': '47',
    'ENGINEERING': '1667',
    'ENGLISHLANGUAGEARTS': '3',
    'ESLENGLISHASASECONDLANGUAGE': '11',
    'FOODSERVICE': '575',
    'FRENCHIMMERSION': '883',
    'GIFTEDTALENTEDEDUCATION': '135',
    'HEALTHEDUCATION': '24',
    'HISTORY': '1211',
    'HOMEECONOMICSCONSUMERSCIENCE': '19',
    'HUMANRESOURCES': '1545',
    'HUMANRESOURCESDIRECTOR': '166',
    'HUMANITIES': '63',
    'JAPANESEIMMERSION': '24217',
    'JOURNALISM': '3377',
    'JOURNALISMEDUCATION': '137',
    'LAW': '800',
    'LIBRARYSCIENCEMEDIATECH': '25',
    'LITERACYCOACH': '1547',
    'LITERATURE': '960',
    'MAINTENANCE': '3902',
    'MANDARINIMMERSION': '8379',
    'MARKETING': '770',
    'MATHEMATICSEDUCATION': '5',
    'MONTESSORISCHOOL': '18366',
    'MULTIPLESUBJECTSUNSPECIFIED': '238',
    'MUSICGENERAL': '8',
    'MUSICINSTRUMENTAL': '138',
    'MUSICVOCAL': '139',
    'NURSESCHOOLNURSE': '140',
    'OCCUPATIONALTHERAPIST': '141',
    'ONLINEINSTRUCTORETEACHING': '8954',
    'OTHER': '21',
    'PHYSICALEDUCATION': '10',
    'PHYSICALTHERAPIST': '142',
    'PRINCIPAL': '437',
    'PRINCIPALELEMENTARY': '161',
    'PRINCIPALHIGHSCHOOL': '163',
    'PRINCIPALMIDDLESCHOOL': '162',
    'PSYCHOLOGISTSCHOOLPSYCHOLOGIST': '143',
    'READING': '15',
    'RELIGIOUSSTUDIES': '499',
    'SCIENCEBIOLOGY': '65',
    'SCIENCECHEMISTRY': '144',
    'SCIENCEEARTHPHYSICAL': '145',
    'SCIENCEGENERAL': '6',
    'SCIENCEINTEGRATEDSCIENCE': '15279',
    'SCIENCEPHYSICS': '1231',
    'SCIENCEPSYCHOLOGY': '2440',
    'SECRETARY': '881',
    'SOCIALSTUDIESEDUCATION': '13',
    'SOCIALWORKER': '146',
    'SPANISHIMMERSION': '1694',
    'SPECIALEDAUTISM': '147',
    'SPECIALEDDUALCERTGENSPEC': '4',
    'SPECIALEDEARLYCHILDHOOD': '148',
    'SPECIALEDEMOTIONALBEHAVIORALDISORDER': '57',
    'SPECIALEDGENERAL': '1628',
    'SPECIALEDHEARINGIMPAIRED': '150',
    'SPECIALEDLEARNINGDISABILITY': '151',
    'SPECIALEDMENTALRETARDATION': '152',
    'SPECIALEDMILDMODERATEDISABILITIES': '153',
    'SPECIALEDMULTICATEGORICAL': '154',
    'SPECIALEDSEVEREPROFOUNDDISABILITIES': '155',
    'SPECIALEDVISUALLYIMPAIRED': '156',
    'SPEECHEDUCATION': '157',
    'SPEECHPATHOLOGIST': '158',
    'SUPERINTENDENT': '167',
    'TECHNOLOGYEDUCATION': '159',
    'THEATERDRAMA': '20',
    'TRANSPORTATION': '2628',
    'VOCATIONALEDUCATION': '160',
    'WORLDLANGUAGES': '9',
}

SELECT_GRADES = "ctl00$lstGradeID"
GRADES = {
    'BIRTHPREK': '22',
    'EARLYCHILDHOOD': '23',
    'ELEMENTARYSCHOOL': '24',
    'MIDDLESCHOOL': '25',
    'HIGHSCHOOL': '26',
    'PREK': '1',
    'K': '2',
    '1': '3',
    '2': '4',
    '3': '5',
    '4': '6',
    '5': '7',
    '6': '8',
    '7': '9',
    '8': '10',
    '9': '11',
    '10': '12',
    '11': '13',
    '12': '14',
    'POSTHSGED': '15',
    'COLLEGE2YEAR': '20',
    'COLLEGE4YEAR': '21',
    'OTHER': '18',
}

PAGINATION_RE = re.compile('''href="javascript:__doPostBack\(&#39;ctl00\$dgrResults\$ctl(29|104|54)\$ctl(\d+)&#39;,&#39;&#39;\)''')


try:
    import local_settings as settings
except ImportError:
    pass


def varify(s):
    # Remove invalid characters
    s = re.sub('[^0-9a-zA-Z_]', '', s)
    return s.upper()


def parse_table(html):
    soup = BeautifulSoup(html)
    table = soup.find("table", {'class' : 'resultTable'})

    # Get Headers
    headers = []
    header_cells = table.find('tr').find_all('th')
    for cell in header_cells:
        headers.append(cell.text)

    jobs = []
    for row in table.findAll('tr')[1:]:
        columns = row.findAll('td')

        job = defaultdict(str)
        for i, header in enumerate(headers):
            try:
                job[header] = columns[i].text.strip('\r\n')
            except IndexError:
                job[header] = ''
        jobs.append(job)

    return jobs


def get_jobs():
    br = mechanize.Browser()

    # User agent to work around ASP.Net issues
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    print "Opening Login Page"
    br.open('https://applicant.edzapp.com/login.aspx')
    br.select_form(name="Form2")
    br["email"] = settings.EMAIL
    br["password"] = settings.PASSWORD

    print "Logging into Edzapp"
    homepage = br.submit()

    print "Opening Job Search Page"
    search = br.follow_link(text='Search Jobs')

    # Job Search Form
    br.select_form(name="Form1")

    # Get variable names
    #subjects =  br.form.controls[13].get_items()
    #for s in subjects:
            #print "'{0}': '{1}',".format(varify(s.attrs['label']), s.name)

    # Set region to US only
    br[SELECT_REGIONS] = [REGIONS['US']]

    # Submit form to load State Select
    br.submit(SELECT_STATES_BTN)
    br.select_form(name="Form1")

    # Set States/Provinces
    br[SELECT_REGIONS] = [STATES['OREGON']]

    #~ # Select Fulltime and temporary jobs
    #~ br.form.find_control(name=SCHEDS['FULLTIME']).items[0].selected = True
    #~ br.form.find_control(name=SCHEDS['TEMPORARY']).items[0].selected = True

    #~ # Select art and elementary jobs
    #~ br[SELECT_SUBJECTS] = [
                    #~ SUBS['ARTVISUALEDUCATION'],
                    #~ SUBS['ELEMENTARYEDUCATIONMULTIPLESUBJECTS'],
    #~ ]

    # Needed for submitting later to get additional results pages
    search_control = br.form.find_control(name=SEARCH_BTN)

    print "Running Job Search"
    response = br.submit(name=SEARCH_BTN)

    ## Show 100 Results per page ##

    br.select_form(name="Form1")

    # Add search button to form for br.submit to work
    br.form.controls.append(search_control)
    br['ctl00$ddlResults'] = ['100']
    br.set_all_readonly(False)
    br["__EVENTTARGET"] = 'ctl00$ddlResults'
    br["__EVENTARGUMENT"] = ''

    print "Show 100 items per page"
    response = br.submit(SEARCH_BTN)

    print "Page 1"

    i = 0
    pages = []
    while True:
        html = response.read()
        pages.append(html)

        codes = PAGINATION_RE.findall(html)
        print codes

        try:
            page_size_code = codes[0][0]
            print "Page size code: ", page_size_code
        except IndexError:
            print "Last Page"
            break

        page_num_codes = zip(*codes)[1]
        print "Page number codes", page_num_codes

        # Set page range using initial pages found
        if i == 0:
            page_range = frozenset(list(page_num_codes) + ['00'])
            print "Page Range: ", page_range

        current_page = page_range.difference(page_num_codes)
        print "Current Page: ", current_page

        next_page = int(list(current_page)[0]) + 1
        print next_page
        if next_page in map(int, page_num_codes):

            br.select_form(name="Form1")

            # Add search button to form for br.submit to work
            br.form.controls.append(search_control)

            br.set_all_readonly(False)
            eventtarget = 'ctl00$dgrResults$ctl{0}$ctl{1:02d}'.format(
                                      page_size_code,
                                      next_page
                                  )
            print eventtarget
            br["__EVENTTARGET"] = eventtarget
            br["__EVENTARGUMENT"] = ''
            response = br.submit(SEARCH_BTN)
            print "Page {0}".format(i+2)
        else:
            break

        i += 1

    return pages


def get_saved_jobs(email, password):
    br = mechanize.Browser()
    br.open('https://applicant.edzapp.com/login.aspx')
    br.select_form(name="Form2")
    br["email"] = email
    br["password"] = password
    homepage = br.submit()
    saved_html = br.follow_link(text='Saved Jobs')

    return saved_html


if __name__ == "__main__":

    jobs_html = get_jobs()
    jobs = []
    for page in jobs_html:
        jobs.extend(parse_table(page))

    print "Saving jobs to file: jobs.pkl"
    import pickle
    with open('jobs.pkl', 'wb') as f:
        pickle.dump(jobs, f)

    print "Saving jobs to file: jobs.csv"
    import csv
    headers = jobs[0].keys()
    with open('jobs.csv', 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()

        for job in jobs:
            writer.writerow({k:v.encode('utf8') for k,v in job.items()})
