// Login And Register Page .............................................................
const registerLink = document.getElementById('register-link');
const backToLoginLink = document.getElementById('back-to-login');
const card = document.querySelector('.card');

registerLink.addEventListener('click', (e) => {
  e.preventDefault();
  card.classList.add('flipped');
});

backToLoginLink.addEventListener('click', (e) => {
  e.preventDefault();
  card.classList.remove('flipped');
});






// User Information Edit .............................................................

function editImage() {
  const fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.accept = "image/*";
  fileInput.onchange = function(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        document.getElementById("profile-img").src = e.target.result; 
      };
      reader.readAsDataURL(file);
    }
  };
  fileInput.click(); 
}
function editProfile() {
  document.getElementById("user-profile-info").style.display = "none";
  document.getElementById("edit-profile-form").style.display = "block";
}

function saveProfile() {
  const updatedProfile = {
    name: document.getElementById("name").value,
    lastName: document.getElementById("last-name").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    address: document.getElementById("address").value,
    taxNumber: document.getElementById("tax-number").value,
    postalCode: document.getElementById("postal-code").value
  };

  if (!updatedProfile.name || !updatedProfile.lastName || !updatedProfile.email || !updatedProfile.phone) {
    alert("Please fill out all required fields.");
    return;
  }

  updateUserProfileInfo(updatedProfile);

  document.getElementById("edit-profile-form").style.display = "none";
  document.getElementById("user-profile-info").style.display = "block";
  
  document.getElementById("confirmation-modal").style.display = "block";
}

function updateUserProfileInfo(updatedProfile) {
  const profileDetails = document.querySelectorAll(".profile-details-user-info p");

  profileDetails[0].innerHTML = `<strong>Name:</strong> ${updatedProfile.name}`;
  profileDetails[1].innerHTML = `<strong>Last Name:</strong> ${updatedProfile.lastName}`;
  profileDetails[2].innerHTML = `<strong>Email Address:</strong> ${updatedProfile.email}`;
  profileDetails[3].innerHTML = `<strong>Address:</strong> ${updatedProfile.address}`;
  profileDetails[4].innerHTML = `<strong>Phone Number:</strong> ${updatedProfile.phone}`;
  profileDetails[5].innerHTML = `<strong>Tax Number:</strong> ${updatedProfile.taxNumber}`;
  profileDetails[6].innerHTML = `<strong>Postal Code:</strong> ${updatedProfile.postalCode}`;
}


function closeModal() {
  document.getElementById("confirmation-modal").style.display = "none";
}

function closeEditForm() {
  document.getElementById("edit-profile-form").style.display = "none";
  document.getElementById("user-profile-info").style.display = "block";
}






// User Dashboard Email .............................................................

function showFolder(folder) {
  if (folder === 'inbox') {
      document.getElementById('inbox-messages').style.display = 'block';
      document.getElementById('sent-messages').style.display = 'none';
      document.querySelector('.mailbox-header h4').innerText = 'Inbox';
  } else if (folder === 'sent') {
      document.getElementById('inbox-messages').style.display = 'none';
      document.getElementById('sent-messages').style.display = 'block';
      document.querySelector('.mailbox-header h4').innerText = 'Sent';
  }
}

function markAll() {
  let checkboxes = document.querySelectorAll('.mail-item input[type="checkbox"]');
  checkboxes.forEach(checkbox => {
      checkbox.checked = true;
  });
}

function deleteSelected() {
  let checkboxes = document.querySelectorAll('.mail-item input[type="checkbox"]:checked');
  checkboxes.forEach(checkbox => {
      checkbox.closest('.mail-item').remove();
  });
}

function refreshInbox() {
  document.getElementById("loader").style.display = "flex";

  setTimeout(function() {
      document.getElementById("loader").style.display = "none";
      alert("Inbox refreshed! No new messages.");
  }, 2000);
}









