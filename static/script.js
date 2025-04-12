document.getElementById("generate-btn").addEventListener("click", async () => {
    const excuseElement = document.getElementById("excuse");

    excuseElement.textContent = "Loading...";

    try {
        const response = await fetch("/get_excuse");
        if (!response.ok) {
            throw new Error("Failed to fetch excuse");
        }

        const data = await response.json();
        excuseElement.textContent = data.excuse;
    } catch (error) {
        excuseElement.textContent = "Oops! Something went wrong.";
    }
});
