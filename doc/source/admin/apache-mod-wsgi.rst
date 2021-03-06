..
      Except where otherwise noted, this document is licensed under Creative
      Commons Attribution 3.0 License.  You can view the license at:

          https://creativecommons.org/licenses/by/3.0/


Installing API behind mod_wsgi
==============================

#. Install the Apache Service::

    Fedora 21/RHEL7/CentOS7:
      sudo yum install httpd

    Fedora 22 (or higher):
      sudo dnf install httpd

    Debian/Ubuntu:
      apt-get install apache2

#. Copy ``etc/apache2/watcher.conf`` under the apache sites::

    Fedora/RHEL7/CentOS7:
      sudo cp etc/apache2/watcher /etc/httpd/conf.d/watcher.conf

    Debian/Ubuntu:
      sudo cp etc/apache2/watcher /etc/apache2/sites-available/watcher.conf

#. Edit ``<apache-configuration-dir>/watcher.conf`` according to installation
   and environment.

   * Modify the ``WSGIDaemonProcess`` directive to set the ``user`` and
     ``group`` values to appropriate user on your server.
   * Modify the ``WSGIScriptAlias`` directive to point to the
     watcher/api/app.wsgi script.
   * Modify the ``Directory`` directive to set the path to the Watcher API
     code.
   * Modify the ``ErrorLog and CustomLog`` to redirect the logs to the right
     directory.

#. Enable the apache watcher site and reload::

    Fedora/RHEL7/CentOS7:
      sudo systemctl reload httpd

   Debian/Ubuntu:
    sudo a2ensite watcher
    sudo service apache2 reload
