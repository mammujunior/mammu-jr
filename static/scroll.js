if (window.innerWidth <= 768) {

    const cards = document.querySelectorAll(".card");

    // Scroll reveal
    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15 }
    );

    cards.forEach(card => {
        observer.observe(card);

        // Tap to expand
        card.addEventListener("click", () => {
            card.classList.toggle("expanded");
        });
    });
}
