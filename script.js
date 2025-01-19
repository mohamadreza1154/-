function addReminder() {
    const dateInput = document.getElementById('reminder-date');
    const dateValue = dateInput.value;
    if (dateValue) {
        const reminderList = document.getElementById('reminder-list');
        const listItem = document.createElement('li');
        listItem.textContent = Reminder set for: ${dateValue};
        reminderList.appendChild(listItem);
        dateInput.value = '';
    } else {
        alert('Please select a date.');
    }
}