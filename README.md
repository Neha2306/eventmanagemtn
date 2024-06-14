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