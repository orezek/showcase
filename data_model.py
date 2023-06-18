# PAGE DATA and METADATA
# headers - metadata
website_metadata = {"contacts": "Contacts", "skills": "Skills", "certifications": "Certifications",
                    "education": "Education", "interests": "Interests", "profile_summary": "Profile Summary",
                    "work_experience": "Work Experience", "linkedin": "LinkedIn", "github": "Github",
                    "about_me": "About Me", "page_title": "Rezek Oldrich CV"}

# info about the page as a project
footer_about_info = """The page is made up of standard HTML, CSS, some Javascript 
code. However, it is a Flask application and runs fully on AWS Elastic Beansltalk. The components used are; simple 
EC2 instance along with ELB in front of it, DynamoDB as its backend, S3 for media storage, Route53 for DNS and domain 
name registration. I am also utilising AWS CodePipeline to automate deployment when the repo in GitHub gets updated. """

footer_data = {"footer_about_info": footer_about_info}

# text for the navbar
aws_logo_link = "https://d0.awsstatic.com/logos/powered-by-aws-white.png"
aws_link = "https://aws.amazon.com/what-is-cloud-computing"
navbar_metadata = {"aws_logo": aws_logo_link, "aws_link": aws_link}

# USER DATA SECTION

personal_mini_header_v1 = "Cloud Engineer, Developer and Technology Enthusiast"
personal_mini_header = "System/Network Admin and Technology Enthusiast"

# interests section
interests = ["Technology",
             "Blockchain",
             "Finance",
             "Sport",
             "Photography",
             "History",
             "Philosophy",
             "Travelling",
             "Exploring"]

# skills section along with competency score
skills = {"AWS Cloud": 80,
          "Windows Server": 82,
          "MS Sharepoint": 60,
          "Networking": 75,
          "Linux": 45,
          "VM Ware": 70,
          "Veeam": 60,
          "Python": 50,
          "HTML": 55,
          "Problem Solving": 90, }

# job titles
job_titles = {"sys_admin": "System Administrator", "it_man": "IT Manager", "net_admin": "Network Administrator"}

profile_summary_data_prod = """I have been in the IT industry for more than a decade, spending time in various roles. 
I started in a support role (L1 & L2) back in 2008, and progressively moved on to more technically advanced roles 
mainly managing IT infrastructure and administering various systems before moving to a managerial position and 
freelancing. Over the years, I have acquired 'industry standard' skills through exposure to various products and 
vendors from industry household names and infrastructure environments, such as VMware, Veeam, Microsoft, Cisco, 
Aruba, Ubiquity, Ruckus, Oracle, and other software or hardware products. I am proficient in managing infrastructure 
and IT operations from day to day tasks to complex project management, ensuring uninterrupted business continuity and 
optimized performance. My experience also extends to troubleshooting and resolving diverse technical issues, 
capacity planning, devising disaster recovery strategies, and managing vendor relations. The wealth of my practical 
knowledge is complemented by my proven ability to lead teams and successfully manage resources, owing to my later 
years in managerial roles. I've also been exposed to the world of freelancing where I have assisted businesses in 
assessing and enhancing their IT infrastructure. This comprehensive journey has equipped me with a deep understanding 
of the IT landscape and its continuous evolution, making me adaptable and forward-thinking. Regardless of the 
technology or challenge at hand, I've always been committed to leveraging my extensive skill set to drive business 
growth and ensure well functioning IT environment."""


soitron_job_description_data = """I am part of a small group of IT professionals responsible for managing and 
supporting the IT infrastructure, as well as other office hardware and client computers, at multiple offices in 
Brussels, Belgium. We were hired to fully outsource the IT operations of a large international customer and provide a 
range of services, including consulting, server and network management, and client support. My duties include 
ensuring the smooth functioning of IT systems, troubleshooting issues, and collaborating with my colleagues to 
provide comprehensive support to our clients. """


zuri_job_description_data = """I was in charge of managing the IT department at a luxurious hotel located in 
Zanzibar, Tanzania. My primary responsibilities included ensuring that the IT operations ran smoothly around the 
clock for both internal and external customers, with a particular focus on sticking to a strict budget during the 
pandemic. I led a small team of local staff and together, we achieved excellent results in our tasks. Given the 
nature of the hotel, it was essential to maintain constant vigilance and to execute tasks with a high level of speed 
and quality. The job was quite varied and required me to handle a range of duties, such as financial planning, 
hiring, negotiations with vendors, communication with government agencies, sourcing and purchasing hardware, 
and overseeing the server, network, and application infrastructure of the property, which covered 14 acres and had 
around 220 active access points, over 11km of optical cabling, and more than 350 employees or 100 high-profile paying 
clients. I am happy to provide references upon request."""


velaa_job_description_data = """I was responsible for maintaining and supporting the large network, 
server infrastructure, applications, and end-client devices on a secluded private island in the Maldives, 
which was used by top 1% net worth individuals. The environment was extremely demanding, requiring me to handle a 
wide range of tasks and projects with fast resolution times. These duties included monitoring and managing the 
network and server infrastructure, troubleshooting and resolving issues with applications and end-client devices, 
implementing security measures to protect against cyber threats, and collaborating with team members to ensure the 
smooth operation of the IT systems. Despite the challenges, I was able to consistently deliver high-quality work and 
meet the expectations of our clients. If you require further information about my experience and skills, I am happy 
to provide references upon request."""

olympus_job_description_data = """I was responsible for maintaining a Microsoft Sharepoint 2013 and 2016 server farm 
and building business applications and workflows for internal clients using Nintex workflow software. This position 
required me to have a strong understanding of Sharepoint and the ability to troubleshoot and resolve issues as they 
arose. I worked closely with the internal IT team and our clients to ensure that the server farm was running 
efficiently and that the business applications and workflows, developed using Nintex software, were meeting the needs 
of the organization. In addition to my technical responsibilities, I also contributed to the development of policies 
and procedures related to Sharepoint and participated in regular training and professional development activities to 
stay up-to-date on the latest technology trends and best practices in the field. Overall, my experience at Olympus 
helped me to build valuable skills in system administration and further my career in the IT industry. """

# links to social media and certifications
linkedin_link = "https://www.linkedin.com/in/oldrich-rezek-175503229/"
github_link = "https://github.com/orezek/curriculum"

aws_dev_link = "https://www.credly.com/badges/56210d28-1b2e-4835-acbd-a71978577fb9/public_url"
aws_arch_link = "https://www.credly.com/badges/e247032c-7f99-45a1-84b4-0a0760de2808/public_url"
aws_fond_link = "https://www.credly.com/badges/9c64e8d6-4632-41b6-aa12-29c521802fb6/public_url"

cisco_ccna_link = "https://www.credly.com/badges/edd4c598-577a-4ce0-9d87-7f4ce0340dfb/public_url"

user_data = {"user_info": {"user_full_name": {"name": "Oldrich", "surname": "Rezek"},
                           "user_bio": {"dob": "02051984", "age": "39", "nationality": "czech",
                                        "place_of_birth": "trinec",
                                        "country": "czechia", "marital_status": "single"},
                           "user_address": {"street": "quai au foin", "house_no": "41", "city": "brussels",
                                            "postal_code": "1000",
                                            "country": "belgium"},
                           "user_contacts": {"email": "orezek@seznam.cz", "phone_no_cz": "+420 608 840 502",
                                             "phone_no_be": "+320 497 127 267",
                                             "linkedin": linkedin_link, "github": github_link}},
             "user_miscellaneous": {"languages": {"czech": "Czech", "english": "English"},
                                    "whoami": personal_mini_header,
                                    "greeting": "Hey, I'm"},
             "profile_info": {"profile_summary": profile_summary_data_prod},
             "work_experience": {"soitron": {"job_title": job_titles["sys_admin"],
                                             "job_company": "Soitron s.r.o - Brussels, Belgium - June 2022 - present",
                                             "job_description": soitron_job_description_data},
                                 "zuri": {"job_title": job_titles["it_man"],
                                          "job_company": "Zuri Zanzibar hotel and resort - Zanzibar - June 2019 - May "
                                                         "2022", "job_description": zuri_job_description_data},
                                 "velaa": {"job_title": job_titles["net_admin"],
                                           "job_company": "Velaa Private Island - Maldives - October 2018 - May 2019",
                                           "job_description": velaa_job_description_data},
                                 "olympus": {"job_title": job_titles["sys_admin"],
                                             "job_company": "Olympus sro - Prague Czech "
                                                            "Republic - April 2016 - "
                                                            "September 2018",
                                             "job_description": olympus_job_description_data}},
             "skills": skills,
             "certification": {"aws_dev": aws_dev_link, "aws_arch": aws_arch_link, "aws_fond": aws_fond_link,
                               "cisco_ccna": cisco_ccna_link},
             "education": {"institution": "Technical colleague Kolin, Czech Republic",
                           "field": "Mechanical engineering"},
             "interests": interests
             }
