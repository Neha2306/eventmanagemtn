<h3>Event Management System Documentation</h3>

<h3>Introduction</h3>
<p>Welcome to the Event Management System documentation. This system allows users to create, update, delete, and view events in both card view and calendar view. To access the system, users need to register and log in.</p>

<h3>Event Categories</h3>
<p>Events in the system are divided into two categories:</p>

1. <b>Casual Events (Not RSVP):</b> Organizers can invite any registered user(s) to attend the event.
2. <b>Events (RSVP):</b> Organizers can create events where registered users who want to attend can confirm their participation.

<h3>Home (Dashboard) Sections</h3>
<p>The Home section of the dashboard comprises three main sections:</p>

1. <b>Upcoming Events (RSVP Only):</b>
    <ul>
    <li>Users can view all RSVP events for which they have not yet confirmed their attendance.</li>
    <li>Organizers cannot view their own created events in this section.</li>
    </ul>

2. <b>Confirmed Events (RSVP):</b>
    <ul>
    <li>Users can view all RSVP confirmed events here.</li>
    <li>Calendar view is available for easy navigation.</li>
    </ul>

3. <b>Casual Event Invite:</b>
    <ul>
    <li>Lists all events for which the user has been invited.</li>
    </ul>

<h3>Organizers and Special Access</h3>
<p>Users need special access to become organizers of events. Admins can grant users organizer privileges by considering them as Staff Members from the admin panel.</p>

<hr>

<h3>File Organization</h3>
<ul>
    <li><b>/eventsmanagement</b> : Root directory of the Django project.
        <ul>
            <li><b>/events</b> : Django app for managing events.
                <ul>
                    <li><b>/migrations</b> : Database migrations for the events app.</li>
                    <li><b>/templates</b> : HTML templates for rendering event-related pages.</li>
                    <li><b>/static/css/custom.css</b> : Contains custom CSS styles for the web application, organized within the "css" folder under the "static" directory</li>
                    <li><b>/models.py</b> : Defines the database models for events.</li>
                    <li><b>/views.py</b> : Defines the views for handling event-related requests.</li>
                    <li><b>/urls.py</b> : Specifies the URL routing patterns and their corresponding view functions.</li>
                    <li><b>/userdata.py</b> : Defines a custom user creation form extending Django's built-in UserCreationForm to include additional fields for first name and last name.</li>
                </ul>
            </li>
            <li><b>manage.py</b> : Django project management script.</li>
            <li><b>requirements.txt</b> : Lists the project dependencies.</li>
        </ul>
    </li>
</ul>

<hr>

<h3>Installation</h3>
<p>Follow these steps to set up and run the project locally:</p>
<ul>
  <li><b>Clone the repository:</b><br>
    <pre>git clone GITURL<br>cd your-project</pre>
  </li>
  <li><b>Set up virtual environment (optional):</b><br>
    <pre>python -m venv env<br># On Windows<br>env\Scripts\activate<br># On macOS/Linux<br>source env/bin/activate</pre>
  </li>
  <li><b>Install dependencies:</b><br>
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li><b>Apply migrations:</b><br>
    <pre>python manage.py migrate</pre>
  </li>
  <li><b>Run the development server:</b><br>
    <pre>python manage.py runserver</pre>
  </li>
  <li><b>Create a superuser (optional):</b><br>
    <pre>python manage.py createsuperuser</pre>
  </li>
</ul>

<hr>

<h3>How To Create Events</h3>
<b>Event Details Setup : </b>
<ul>
    <li><b>Event Name:</b> Organizers must provide a unique name for the event.</li>
    <li><b>Event Description:</b> A detailed description or summary of what the event entails.</li>
    <li><b>Event Date:</b> The specific date on which the event will occur.</li>
    <li><b>Event Time:</b> The start time of the event.</li>
    <li><b>RSVP Requirement:</b> Organizers specify whether attendees need to RSVP (confirm their attendance) for the event.</li>
    <li><b>Organizer Selection:</b> When creating the event, administrators select the organizer from a list, along with filling out the rest of the event details.</li>
</ul>
</br>
<b>Event RSVP and Casual Invitation : </b>
<ul>
    <li><b>RSVP vs. Casual Event:</b> If the organizer does not mark the event as requiring RSVP, it is considered a casual event.</li>
    <li><b>Casual Invitation:</b> For casual events, organizers can manually select which users to invite, will appear under the "Casual Invite Section" in the dashboard.</li>
    <li><b>RSVP Confirmation:</b> For events marked as requiring RSVP, users must confirm their attendance, indicating whether they will attend or not.</li>
</ul>
