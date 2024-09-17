window.onload = function() {
    const containerIds = ['container-2', 'container-3', 'container-4'];
    const hiddenDiv = document.getElementById('hidden');

    if (hiddenDiv) {
        // Initially hide the content
        hiddenDiv.style.display = 'none';
        console.log("Set initial display of #hidden to 'none'");

        containerIds.forEach(id => {
            const container = document.getElementById(id);

            if (container) {
                container.addEventListener('click', function() {
                    console.log(`${id} was clicked.`);

                    // Move the hidden div inside the clicked container
                    this.appendChild(hiddenDiv);

                    // Toggle the visibility of the hidden div
                    if (hiddenDiv.style.display === 'block') {
                        hiddenDiv.style.display = 'none';
                        console.log(`Hidden content is now hidden.`);
                    } else {
                        hiddenDiv.style.display = 'block';
                        console.log(`Hidden content is now visible in ${id}.`);
                    }
                });

                console.log(`Click event listener added to #${id}`);
            } else {
                console.error(`Container #${id} not found.`);
            }
        });
    } else {
        console.error("The 'hidden' div was not found!");
    }
};