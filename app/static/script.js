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
                const url = URL.createObjectURL(data);
                resultDiv.innerHTML = `<h2>Uploaded Image:</h2><img src="${url}" alt="Uploaded Image">`;

            } catch (error) {
                console.error("Error during image upload:", error);
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = "<p>Error uploading image. Please try again later.</p>";
            }
        });