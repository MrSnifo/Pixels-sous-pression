document.getElementById('uploadForm').addEventListener('submit', async function(event) {
            event.preventDefault();

            const formData = new FormData();
            const fileInput = document.getElementById('image');
            if (fileInput.files.length === 0) {
                alert("Please select an image to upload.");
                return;
            }

            formData.append('file', fileInput.files[0]);

            try {
                const response = await fetch('/api/upload/', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    throw new Error("Failed to upload image.");
                }

                const data = await response.blob();
                const resultDiv = document.getElementById('result');


                // Make the download button visible
                const url = URL.createObjectURL(data);
                resultDiv.innerHTML = `<h2>Uploaded Image:</h2><img src="${url}" alt="Uploaded Image">`;

                    const downloadButton = document.getElementsByClassName('Download')[0];
                    downloadButton.style.display = "block";

                    // Set up the download functionality
                    downloadButton.onclick = function() {
                        const link = document.createElement('a');
                        link.href = url;
                        link.download = `${url}.webp`; // You can customize the filename here
                        link.click(); // This will trigger the download
                    };



            } catch (error) {
                console.error("Error during image upload:", error);
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = "<p>Error uploading image. Please try again later.</p>";
            }

        });