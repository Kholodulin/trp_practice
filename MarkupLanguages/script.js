$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "recipe.xml",
        dataType: "xml",
        success: function(xml) {
            $(xml).find('recipe').each(function() {
                var title = $(this).find('title').text();
                var ingredients = $(this).find('ingredient').map(function() {
                    return $(this).text();
                }).get().join(', ');
                var instructions = $(this).find('step').map(function() {
                    return $(this).text();
                }).get().join('<br>');

                var recipeHtml = `
                    <div class="recipe">
                        <h2>${title}</h2>
                        <p><strong>Ингредиенты:</strong> ${ingredients}</p>
                        <p><strong>Инструкции:</strong><br> ${instructions}</p>
                    </div>
                `;
                $('#recipes').append(recipeHtml);
            });
        }
    });

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
