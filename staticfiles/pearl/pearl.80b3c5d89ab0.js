'use strict';

const applicationServerPublicKey = 'BKy1hiEm1lJuE3OtKlGTfO5vA07UKDrJoBoi184MdlJEfbg8aVXiSjfjuTZenIvawsn45nSejbITxYge4dXZU2c';

const pushButton = document.querySelector('.js-push-btn');

let isSubscribed = false;
let swRegistration = null;

function burgerMenu() {
    var x = document.getElementById('navbarText');
    if (x.style.display === 'block') {
        x.style.display = 'none';
    } else {
        x.style.display = 'block';
    }
}


console.log("ABOUT TO ENTER FUNCTION");

const check = () => {
    if (!('serviceWorker' in navigator)){
    throw new Error('No Service Worker support!')
    }
    if (!('PushManager' in window)) {
        throw new Error('No Push API Support!')
    }
}

const main = () => {
    check()
}

main()



function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

if ('serviceWorker' in navigator && 'PushManager' in window) {
  console.log('Service Worker and Push are supported');

  navigator.serviceWorker.register('sw.js')
  .then(function(swReg) {
    console.log('Service Worker is registered', swReg);

    swRegistration = swReg;
  })
  .catch(function(error) {
    console.error('Service Worker Error', error);
  });
} else {
  console.warn('Push messaging is not supported');
  pushButton.textContent = 'Push Not Supported';
}

function initializeUI() {
  // Set the initial subscription value
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    isSubscribed = !(subscription === null);

    if (isSubscribed) {
      console.log('User IS subscribed.');
    } else {
      console.log('User is NOT subscribed.');
    }

    updateBtn();
  });
  pushButton.addEventListener('click', function() {
    pushButton.disabled = true;
    if (isSubscribed) {
      // TODO: Unsubscribe user
    } else {
      subscribeUser();
    }
  });

  // Set the initial subscription value
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    isSubscribed = !(subscription === null);

    updateSubscriptionOnServer(subscription);

    if (isSubscribed) {
      console.log('User IS subscribed.');
    } else {
      console.log('User is NOT subscribed.');
    }

    updateBtn();
  });
}

function updateBtn() {
  if (isSubscribed) {
    pushButton.textContent = 'Disable Push Messaging';
  } else {
    pushButton.textContent = 'Enable Push Messaging';
  }

  if (Notification.permission === 'denied') {
    pushButton.textContent = 'Push Messaging Blocked';
    pushButton.disabled = true;
    updateSubscriptionOnServer(null);
    return;
  }

  if (isSubscribed) {
    pushButton.textContent = 'Disable Push Messaging';
  } else {
    pushButton.textContent = 'Enable Push Messaging';
  }

  pushButton.disabled = false;
}


navigator.serviceWorker.register('sw.js')
.then(function(swReg) {
  console.log('Service Worker is registered', swReg);

  swRegistration = swReg;
  initializeUI();
})

function subscribeUser() {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
  .then(function(subscription) {
    console.log('User is subscribed.');

    updateSubscriptionOnServer(subscription);

    isSubscribed = true;

    updateBtn();
  })
  .catch(function(error) {
    console.error('Failed to subscribe the user: ', error);
    updateBtn();
  });
}

function updateSubscriptionOnServer(subscription) {
  // TODO: Send subscription to application server

  const subscriptionJson = document.querySelector('.js-subscription-json');
  const subscriptionDetails =
    document.querySelector('.js-subscription-details');

  if (subscription) {
    subscriptionJson.textContent = JSON.stringify(subscription);
    subscriptionDetails.classList.remove('is-invisible');
  } else {
    subscriptionDetails.classList.add('is-invisible');
  }
}


// 'use strict';

// const applicationServerPublicKey = 'BHdd2PwLOsYaDQQOmqw_8KIIYOQYECWN' +
//   'lat0K8GScnytjV88e6Xifn0GMz7MbScAkxf_kVJhnp-0NrB_P4u6WHw';

// const pushButton = document.querySelector('.js-push-btn');

// let isSubscribed = false;
// let swRegistration = null;

// function urlB64ToUint8Array(base64String) {
//   const padding = '='.repeat((4 - base64String.length % 4) % 4);
//   const base64 = (base64String + padding)
//     .replace(/\-/g, '+')
//     .replace(/_/g, '/');

//   const rawData = window.atob(base64);
//   const outputArray = new Uint8Array(rawData.length);

//   for (let i = 0; i < rawData.length; ++i) {
//     outputArray[i] = rawData.charCodeAt(i);
//   }
//   return outputArray;
// }

// function updateBtn() {
//   if (Notification.permission === 'denied') {
//     pushButton.textContent = 'Push Messaging Blocked.';
//     pushButton.disabled = true;
//     updateSubscriptionOnServer(null);
//     return;
//   }

//   if (isSubscribed) {
//     pushButton.textContent = 'Disable Push Messaging';
//   } else {
//     pushButton.textContent = 'Enable Push Messaging';
//   }

//   pushButton.disabled = false;
// }

// function updateSubscriptionOnServer(subscription) {
//   // TODO: Send subscription to application server

//   const subscriptionJson = document.querySelector('.js-subscription-json');
//   const subscriptionDetails =
//     document.querySelector('.js-subscription-details');

//   if (subscription) {
//     subscriptionJson.textContent = JSON.stringify(subscription);
//     subscriptionDetails.classList.remove('is-invisible');
//   } else {
//     subscriptionDetails.classList.add('is-invisible');
//   }
// }

// function subscribeUser() {
//   const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
//   swRegistration.pushManager.subscribe({
//     userVisibleOnly: true,
//     applicationServerKey: applicationServerKey
//   })
//   .then(function(subscription) {
//     console.log('User is subscribed.');

//     updateSubscriptionOnServer(subscription);

//     isSubscribed = true;

//     updateBtn();
//   })
//   .catch(function(err) {
//     console.log('Failed to subscribe the user: ', err);
//     updateBtn();
//   });
// }

// function unsubscribeUser() {
//   swRegistration.pushManager.getSubscription()
//   .then(function(subscription) {
//     if (subscription) {
//       return subscription.unsubscribe();
//     }
//   })
//   .catch(function(error) {
//     console.log('Error unsubscribing', error);
//   })
//   .then(function() {
//     updateSubscriptionOnServer(null);

//     console.log('User is unsubscribed.');
//     isSubscribed = false;

//     updateBtn();
//   });
// }

// function initializeUI() {
//   pushButton.addEventListener('click', function() {
//     pushButton.disabled = true;
//     if (isSubscribed) {
//       unsubscribeUser();
//     } else {
//       subscribeUser();
//     }
//   });

//   // Set the initial subscription value
//   swRegistration.pushManager.getSubscription()
//   .then(function(subscription) {
//     isSubscribed = !(subscription === null);

//     updateSubscriptionOnServer(subscription);

//     if (isSubscribed) {
//       console.log('User IS subscribed.');
//     } else {
//       console.log('User is NOT subscribed.');
//     }

//     updateBtn();
//   });
// }

// const registersw = async() =>{
//     console.log("STARTING FUNCTION");
//     if ('serviceWorker' in navigator && 'PushManager' in window) {
//         console.log('Service Worker and Push is supported');
//         try {
//             const swReg = await navigator.serviceWorker.register('/static/pearl/sw.js')
//             console.log('Service Worker is registered', swReg);
//             swRegistration = swReg;
//             console.log("Fetching service worker");
    
//         } catch (error) {
//             console.error('Service Worker Error', error);
//         }
//       } else {
//         console.warn('Push messaging is not supported');
//         pushButton.textContent = 'Push Not Supported';
//       }
// }

// registersw()