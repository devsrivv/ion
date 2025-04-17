document.addEventListener("DOMContentLoaded", () => {
    const toggleBar   = document.querySelector(".senior-dests-toggle");
    const contentBox  = document.querySelector(".senior-dests-content");
    
    if (!toggleBar || !contentBox) 
        return;

    const expandBtn   = toggleBar.querySelector(".senior-dests-expand");
    const collapseBtn = contentBox.querySelector(".senior-dests-collapse");

    
    expandBtn.addEventListener("click", () => {
        contentBox.classList.add("open");
        toggleBar.style.display = "none";
    });

    
    collapseBtn.addEventListener("click", () => {
        contentBox.classList.remove("open");
        toggleBar.style.display = "flex";
    });
});
