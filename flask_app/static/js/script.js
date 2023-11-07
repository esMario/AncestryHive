
function auto_update_age() {
        const dateInput = document.getElementsByName("date_of_birth")[0];
        const ageInput = document.getElementsByName("age")[0];

        dateInput.addEventListener("change", function () {
            const dob = new Date(dateInput.value);
            const today = new Date();
            const age = today.getFullYear() - dob.getFullYear();
            ageInput.value = age;
        });
    }

const dateInput = document.getElementsByName("date_of_birth")[0];
    if (dateInput) {
        console.log("I FOUND YOU DATE OF BIRTH")
        auto_update_age();
    }