# IT Helpdesk Ticket System

A Python-based, terminal-driven IT Helpdesk Ticket Management System built with SQLite and Rich. The project demonstrates role-based access, ticket management, technician assignment, ticket tracking, and administrative reporting.

## Overview

The IT Helpdesk Ticket System helps organize IT support requests in one place. Employees can create tickets and follow their progress, technicians can work on assigned tickets, and administrators can manage users and monitor ticket activity.

The application uses a modular Python structure to separate employee, technician, administrator, and database-related operations.

## Features

### 👤 Employee Module
- Create IT support tickets.
- View tickets created by the logged-in employee.
- Track ticket status.
- Add comments to tickets.
- View profile information and a ticket summary.

### 🛠️ Technician Module
- View tickets assigned to the logged-in technician.
- Update ticket status.
- Add resolution notes.
- View ticket history.
- View technician profile and assigned-ticket statistics.

### ⚙️ Admin Module
- View all helpdesk tickets.
- Assign tickets to active technicians.
- Activate or deactivate user accounts.
- Change eligible user roles.
- View ticket status reports.
- View email logs.
- View the administrator profile.
- Export ticket, user, and report data to Excel.

### 🗄️ Database
The project uses SQLite to store application data. The repository includes database-related modules for:

- User accounts
- Tickets
- Ticket comments
- Ticket history
- OTP verification records
- Email logs
- Ticket attachments

### 📊 Excel Export
The `Admin/ExportExcel.py` module uses OpenPyXL to export records to Excel workbooks.

### 🖥️ Terminal Interface
The Rich library provides formatted menus, tables, and colored terminal messages.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| SQLite | Relational database |
| SQL | Data retrieval and modification |
| Rich | Terminal menus and tables |
| OpenPyXL | Excel workbook export |
| bcrypt | Password-hashing library imported in the login module; hashing still needs to be enabled in the current implementation |

## Project Structure

```text
IT-HelpDesk-Ticket-System/
│
├── Admin/
│   ├── AdminMenu.py
│   ├── Assign_Ticket.py
│   ├── ExportExcel.py
│   ├── Manage_User_Account.py
│   ├── My_Profile.py
│   ├── View_All_Tickets.py
│   ├── View_Email_Logs.py
│   └── View_Ticket_Reports.py
│
├── Connection/
│   ├── ConfigureDB.py
│   ├── Login.py
│   ├── user.py
│   ├── tickets.py
│   ├── ticket_comments.py
│   ├── ticket_history.py
│   ├── otp_verification.py
│   ├── email_logs.py
│   ├── ticket_attachments.py
│   └── helpdesk.db
│
├── Employee/
│   ├── EmployeeMenu.py
│   ├── Create_Ticket.py
│   ├── ViewTicket.py
│   ├── Track_Ticket_Status.py
│   ├── Add_Comments.py
│   └── My_Profile.py
│
├── Technician/
│   ├── TechnicianMenu.py
│   ├── View_Assigned_Tickets.py
│   ├── Update_Ticket_Status.py
│   ├── Add_Resolution_Notes.py
│   ├── View_Ticket_History.py
│   └── My_Profile.py
│
├── main.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/SiddheshPardale/IT-HelpDesk-Ticket-System.git
cd IT-HelpDesk-Ticket-System
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install rich openpyxl bcrypt
```

SQLite is included with standard Python installations, so a separate SQLite package is not normally required.

### 4. Configure the database path

Open `Connection/ConfigureDB.py` and verify that `DATABASE_PATH` points to the intended `helpdesk.db` file.

The current code contains a machine-specific Windows directory. Update it before running the application on another computer.

### 5. Run the application

From the project root:

```bash
python main.py
```

Use the registration option to create an employee account, then log in to access the appropriate role-based menu. An administrator and technician account must be available in the database to test those menus.

## Application Workflow

1. The user opens the application and registers or logs in.
2. The application retrieves the user's role.
3. The corresponding Employee, Technician, or Admin menu is displayed.
4. The user performs the permitted ticket-management operations.
5. Changes are stored in the SQLite database.
6. Administrators can review ticket data and export selected records to Excel.

## Testing

Before using the application with important data, verify:

- Registration and login with valid and invalid credentials.
- Access to the correct role-based menu.
- Ticket creation, viewing, assignment, and status updates.
- Ticket comments and history.
- User activation and role changes.
- Excel export and the contents of generated workbooks.
- Database persistence after restarting the application.

Some workflows and security checks still require validation in the current implementation. In particular, password hashing, OTP expiry verification, ticket-history recording, and ownership checks should be addressed before treating the system as production-ready.

## Future Improvements

- Complete password hashing and secure OTP verification.
- Add email notifications through an email service.
- Record every ticket status transition in the history table.
- Add ticket attachment upload and download workflows.
- Improve input validation and exception handling.
- Add search, filtering, and pagination for large ticket lists.
- Make database configuration portable across systems.
- Add automated tests for database operations and role permissions.

## Learning Objectives

This project provides practical experience with Python modular programming, SQLite connectivity, SQL queries, CRUD operations, role-based application flows, exception handling, terminal interfaces, and Excel report generation.

## Author

**Siddhesh Pardale**

GitHub: [@SiddheshPardale](https://github.com/SiddheshPardale)

## License

This project is intended for learning and demonstration. Add a license file if you intend to distribute or reuse the project under specific terms.

