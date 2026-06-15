from django.core.exceptions import ValidationError

def validate_no_ban_words(value):
    bad_words = ['ban_word', 'ban_word1']
    lowered = value.lower()
    for w in bad_words:
        if w in lowered:
            raise ValidationError('Текст содержит недопустимое слово, уберите слово или будете забанены.')

def validate_summary_length(value):
    if len(value.strip()) < 5:
        raise ValidationError('Краткое описание должно быть не менее 5 символов.')
