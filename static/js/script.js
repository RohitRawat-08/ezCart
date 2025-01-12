// Wait until the DOM content is loaded


document.addEventListener("DOMContentLoaded", () => {
    const addAddressBtn = document.querySelector(".add_address_btn"); // Button to toggle the form
    const formData = document.querySelector(".Form_data"); // The form container

    // Event listener for toggling form visibility
    addAddressBtn.addEventListener("click", () => {
        if (formData.style.display === "block") {
            formData.style.display = "none"; // Hide form
        } else {
            formData.style.display = "block"; // Show form
        }
    });
});
