> [!TIP]
> Helpful advice for doing things better or more easily.

How to run the code:
Step 0: Download files form Github
  1. Opet Terminal and choose repository where you want to clone files from Github
  2. Use following command for cloning by SSH connection `git clone [link_form_the_repo]`

       
Step 1: Creat virtual environment

    python3 -m venv [name_of_your_environment]

Step 2: Enter in environment

    source [name_of_your_environement]/bin/activate

Step 3: Install all needed lybrarys 

    pip install -r requirements.txt

Step 4: Setup nginx with flask

1. Create file with your app name `sudo vim /etc/nginx/sites-available/file_name`

2. Past the code
  
        server {
        listen 80;
        server_name myapp.com;
  
           location / {
              proxy_pass http://127.0.0.1:5000;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
           }
        }

3. Enable the Nginx server block configuration `sudo ln -s /etc/nginx/sites-available/file_name /etc/nginx/sites-enabled/`
   
4. Test the Nginx configuration: `sudo nginx -t and restart sudo service nginx restart`

5. Run in background

       export FLASK_APP=app.py
       flask run --host=0.0.0.0 &



Step 5: Create the service structure
 1. To see the status of the systemctl type sudo systemctl status.
 2. to create the file of the service `sudo systemctl --force --full edit web_application.service`
 3. File need to be located `/etc/systemd/system/web_application.service`
 4. if you are using venv just add this to you service file
        [Unit]
        Description=Gunicorn instance to serve myapp
        After=network.target
        
        [Service]
        User=ubuntu
        Group=ubuntu
        WorkingDirectory=/home/ubuntu/web_application
        Environment="PATH=/home/ubuntu/web_application/web_application_venv/bin"
        ExecStart=/home/ubuntu/web_application/web_application_venv/bin/gunicorn --workers 4 --bind 127.0.0.1:8000 app:app
        Restart=always
        
        [Install]
        WantedBy=multi-user.target

5. Enable the service `sudo systemctl enable web_application`
6. check the status `sudo systemctl status web_application.service`
7.` sudo systemctl daemon-reload`
8. start the service `sudo systemctl start web_application.service` and check again check the status `sudo systemctl status web_application.service`
9. Restart the server to check if you nginx server is working.``


Step 5: Deactivate environement 

    deactivate
