# Element Hover Tracker

## Overview
This demo shows how to track which elements players hover their mouse over. It sends the events to the server immediately using oTree's  new live page beta features. Each element is then stored utilizing a custom data model.

## Requirements
This project uses oTree version 5.2.4 but should work with newer versions.

## Details
On the template I added two listeners that listen for mouseenter and mouseleave events on elements with the "tracked_element" class. If these events are fired, a "hover object" is created which stores the element's id as well as the unix timestamp in milliseconds since epoch at the time the mouse enters the element and when it leaves it again. (Make sure that the elements you track do not overlap.)

Whenever a hover object is complete, i.e. the mouse has entered the element and left it again, the information is sent to the server in near real time. On the server, it is stored in a custom model that is linked to the player. A short data export function exports the list of all such events for all sessions, rounds, and players. This can be found on oTree's "Data" tab (the general one, not the one in the session admin interface).

## Note
This project uses beta software which may change quickly. Do not use in production unless you are absolutely sure you tested all edge cases extremely well.
