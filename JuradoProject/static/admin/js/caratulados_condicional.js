document.addEventListener('DOMContentLoaded', function () {
    const provinciaField = document.querySelector('#id_provincia');
    const tribunalField = document.querySelector('.field-tribunal');
    const jurisdiccionField = document.querySelector('.field-jurisdiccion');

    function toggleFields() {
        if (provinciaField.value === 'provincia') {
            tribunalField.style.display = 'block';
            jurisdiccionField.style.display = 'block';
        } else {
            tribunalField.style.display = 'none';
            jurisdiccionField.style.display = 'none';
        }
    }

    // Inicializa el estado de los campos al cargar la página
    toggleFields();

    // Cambia el estado de los campos cuando cambia el valor de 'provincia'
    provinciaField.addEventListener('change', toggleFields);
});
