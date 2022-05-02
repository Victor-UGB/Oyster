'use strict';

const applicationServerPublicKey = 'BKy1hiEm1lJuE3OtKlGTfO5vA07UKDrJoBoi184MdlJEfbg8aVXiSjfjuTZenIvawsn45nSejbITxYge4dXZU2c';

const pushButton = document.querySelector('.js-push-btn');

let isSubscribed = false;
let swRegistration = null;
const buttonState = [document.querySelectorAll('.nav-bar-item')];
let buttonStateList = [];
function showButtonState(){
  console.log(buttonState);
}

function burgerMenu() {
    var x = document.getElementById('navbarText');
    if (x.style.display === 'block') {
        x.style.display = 'none';
    } else {
        x.style.display = 'block';
    }
}

// function showSection(page){
//   document.querySelectorAll("div.post-entry-sub").forEach ("" () => {
//     '.tab-button'.style.display = "none";
//   })
// }

// function showSection(page){
//   x = document.querySelectorAll("div.post-entry-sub")
//   for( i in x){
//     i.style.display = 'none';
//   }

//   document.querySelector('#${page}').style.display = 'block';
// };

// document.addEventListener('DOMContentLoaded', function(){
//   document.querySelectorAll('button').forEach(button =>{
//     button.onclick = function(){
//       showSection(this.dataset.page);
//     }
//   });
// });

// for(var x of buttonState){ console.log(x);}


// document.addEventListener('DOMContentLoaded', ()=>{
//   document.querySelectorAll('button').forEach(button =>{
//     button.onclick = function(){
//       document.querySelector('#image-tab').style.color = button.dataset.color;
//     }
//   })
// });

// function returnTab(){
//   let y = document.getElementById('navigationBar');
//   y.style.right = '-9rem';
//   console.log('Hello World');
// }


// $(window).scroll(function(){
//   var scrollVal = $(this).scrollTop();

//   $(".block-one").css("transform","translate(0px,-"+scrollVal/2+'%)');
//   $(".second-child").css("transform","translate(-20px,-"+scrollVal/2+'%)');
// });

function drawNavbar(){
  let x = document.getElementById('navBarDrawer');
  let y = document.getElementById('navigationBar');
  let z = document.getElementById('tabDiv');
  x.addEventListener('click', function(){
    if (y.style.right == '1rem'){
      y.style.right = '-10rem';
    }else if (y.style.right == '1rem' && window.addEventListener(this.click = true)){
      y.style.right = '-10rem';
      console.log('hide navbar');
    }else{
      y.style.right = '1rem';
    }
  })
  z.addEventListener('click', function(){
    y.style.right = '-9rem';
  })
}

drawNavbar();

function activateButton(buttonState){
  for(let btnState of buttonState){
    buttonStateList.push(btnState);
    console.log(btnState);
    let buttonStateId = btnState.id;
    for(var btnStateItem of buttonStateList)
      if (btnStateItem === 'inactive'){
        btnStateItem = 'active';
      }else{
        btnStateItem = 'inactive';
      }
    return buttonStateId;
  }
  return btnState;
}


function toggleImagedisplay(){
  var podcast = document.getElementById('podcast');
  var vidcast = document.getElementById('vidcast');
  var image = document.getElementById('image');
  var imageTab = document.getElementById('image-tab');
  var videoTab = document.getElementById('video-tab');
  var podcastTab = document.getElementById('podcast-tab');
  activateButton(buttonState);

  if (image.style.display == 'block'){
    image.style.display = 'block';
    vidcast.style.display = 'none';
    podcast.style.display = 'none';
    imageTab.style.backgroundColor = '#383A48';
    podcastTab.style.backgroundColor = 'white';
    videoTab.style.backgroundColor = 'white';
    imageTab.style.color='white'

  }else{
    image.style.display = 'block';
    vidcast.style.display = 'none';
    podcast.style.display = 'none';
    imageTab.style.backgroundColor = '#383A48';
    podcastTab.style.backgroundColor = 'white';
    videoTab.style.backgroundColor = 'white';

  }
}

function toggleVideodisplay(){
  let podcast = document.getElementById('podcast');
  let vidcast = document.getElementById('vidcast');
  let image = document.getElementById('image');
  let buttonState = document.querySelector('button').id;
  var videoTab = document.getElementById('video-tab');
  var imageTab = document.getElementById('image-tab');
  var podcastTab = document.getElementById('podcast-tab');
  activateButton(buttonState);

  if (vidcast.style.display == 'block'){
    vidcast.style.display = 'block';
    podcast.style.display = 'none';
    image.style.display = 'none';
    videoTab.style.backgroundColor = '#383A48';
    imageTab.style.backgroundColor = 'white';
    podcastTab.style.backgroundColor = 'white';
    videoTab.style.color='white'
  }else{
    vidcast.style.display = 'block';
    podcast.style.display = 'none';
    image.style.display = 'none';
    videoTab.style.backgroundColor = '#383A48';
    imageTab.style.backgroundColor = 'white';
    podcastTab.style.backgroundColor = 'white';
    videoTab.style.color='white'
  };
}

function togglePodcastdisplay(){
  let podcast = document.getElementById('podcast');
  let vidcast = document.getElementById('vidcast');
  let image = document.getElementById('image');
  let buttonState = document.querySelector('button').id;
  var podcastTab = document.getElementById('podcast-tab');
  var videoTab = document.getElementById('video-tab');
  var imageTab = document.getElementById('image-tab');
  activateButton(buttonState);

  if (podcast.style.display == 'block'){
    podcast.style.display = 'block';
    image.style.display = 'none';
    vidcast.style.dispaly = 'none';
    podcastTab.style.backgroundColor = '#383A48';
    videoTab.style.backgroundColor = 'white';
    imageTab.style.backgroundColor = 'white';
    podcastTab.style.color='white'
  }else{
    podcast.style.display = 'block';
    image.style.display = 'none';
    vidcast.style.display = 'none';
    podcastTab.style.backgroundColor = '#383A48';
    videoTab.style.backgroundColor = 'white';
    imageTab.style.backgroundColor = 'white';
    podcastTab.style.color='white'
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