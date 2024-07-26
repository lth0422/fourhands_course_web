//
// events.js
//

import { Collapse } from 'bootstrap';

const eventLgs = document.querySelectorAll('.event-lg');

function getSmInstance(target) {
  const eventSm = target.closest('.event').querySelector('.event-sm');
  return new Collapse(eventSm, { toggle: false });
}

function getLgInstances(target) {
  const eventLgs = target.closest('.events').querySelectorAll('.event-lg');
  const eventLgsFiltered = Array.from(eventLgs).filter((eventLg) => eventLg !== target);
  return eventLgsFiltered.map((eventLg) => new Collapse(eventLg, { toggle: false }));
}

eventLgs.forEach((eventLg) => {
  eventLg.addEventListener('show.bs.collapse', (e) => {
    const eventSmInstance = getSmInstance(e.target);
    eventSmInstance.hide();

    const eventLgInstances = getLgInstances(e.target);
    eventLgInstances.forEach((eventLgInstance) => {
      if (eventLgInstance !== e.target) {
        eventLgInstance.hide();
      }
    });
  });

  eventLg.addEventListener('hide.bs.collapse', (e) => {
    const eventSmInstance = getSmInstance(e.target);
    eventSmInstance.show();
  });
});
