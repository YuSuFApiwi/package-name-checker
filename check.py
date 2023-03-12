import webbrowser
import urllib.request,sys

if (len(sys.argv) == 1):
	print("Please specify a list of package names. \nUsage: \npython check.py package_list.txt")
	sys.exit()

pklist_file = sys.argv[1]
try:
	packages = open(pklist_file).readlines()
except:
	print("I/O Error.")
	sys.exit()
url_play = "https://play.google.com/store/apps/details?id="
apps_is_live = []
apps_not_found = []
for i in range(0,len(packages)):
	try:
		package_name = packages[i].replace('\n','')
		print(f"{str(i+1)} : Checking {package_name}... [{str(i+1)}/{str(len(packages))}]")
		response = urllib.request.urlopen(url_play + packages[i])
		html = response.read()
		apps_is_live.append(packages[i])
	except urllib.request.HTTPError:
		apps_not_found.append(packages[i])

#Define the HTML content
html_content = f"""
<html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detective Apiwi</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"/>
    <link
      rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&amp;display=swap" />
    <link rel="stylesheet" href="https://mdbootstrap.com/api/snippets/static/download/MDB5-Pro-Advanced_6.1.0/css/mdb.min.css"/>
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <section class="intro">
      <div class="bg-image h-100"
        style="background-image: url('https://mdbootstrap.com/img/Photos/new-templates/tables/img2.jpg');">
        <div class="mask d-flex align-items-center h-100" style="background-color: rgba(0, 0, 0, 0.25)">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-12">
                <div class="card bg-dark shadow-2-strong">
				  <div class="card-header text-center">
                    <h3>{str(len(apps_is_live))} of {str(len(packages))} apps are found in Google Play Store</h3>
                  </div>
                  <div class="card-body">
                    <div class="table-responsive">
                      <table class="table table-dark table-borderless mb-0">
                        <thead>
                          <tr>
                            <th scope="col-1">N</th>
                            <th scope="col">OPEN</th>
                            <th scope="col">PACKAGE NAME</th>
                            <th scope="col">STATUS</th>
                          </tr>
                        </thead>
                        <tbody>
"""
text_str = ""
counter = 0
for i in range(0, len(apps_not_found)):
	counter += 1
	app_name = apps_not_found[i].replace("\n","")
	text_str += f"""<tr>
				<th scope="row">{counter}</th>
				<td>
					<a href="{url_play + app_name}" target="_blank">
						<i class="fa fa-link fa-2x"></i>
					</a>
				</td>
				<td>{app_name}</td>
				<td><span class="badge badge-danger">NOT FOUND</span></td>
			</tr>"""
for i in range(0, len(apps_is_live)):
	counter += 1
	app_name = apps_is_live[i].replace("\n","")
	text_str += f"""<tr>
				<th scope="row">{counter}</th>
				<td>
					<a href="{url_play + app_name}" target="_blank">
						<i class="fa fa-link fa-2x"></i>
					</a>
				</td>
				<td>{app_name}</td>
				<td><span class="badge badge-success">IS AVAILABLE</span></td>
			</tr>"""
html_content += text_str
html_content += """</tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>"""

with open('verification_page.html', 'w') as f:
    f.write(html_content)
    
webbrowser.open('verification_page.html')