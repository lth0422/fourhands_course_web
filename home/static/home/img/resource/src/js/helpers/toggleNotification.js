import { Toast } from 'bootstrap';

export default function toggleNotification(message) {
  const notification = document.getElementById('notification');
  const toast = new Toast(notification);

  notification.querySelector('.toast-body').innerHTML = message;
  toast.show();
}
