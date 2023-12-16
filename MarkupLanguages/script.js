$(document).ready(function() {
    // Загрузка данных из JSON
    $.getJSON("recipe.json", function(data) {
        $.each(data.recipes, function(index, recipe) {
            var title = recipe.title;
            var ingredients = recipe.ingredients.join(', ');
            var instructions = recipe.instructions.join('<br>');

            var recipeHtml = `
                <div class="recipe">
                    <h2>${title}</h2>
                    <p><strong>Ингредиенты:</strong> ${ingredients}</p>
                    <p><strong>Инструкции:</strong><br> ${instructions}</p>
                </div>
            `;
            $('#recipes').append(recipeHtml);
        });
    });
});
