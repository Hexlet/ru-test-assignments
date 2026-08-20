# Тестовое задание

> Локальная копия. Источник: <https://github.com/magnum-design/photohunt-test-task>
Необходимо написать имплементацию компонента `<GenericModal/>`. Компонент должен принимать заголовок, подзаголовок, children и две callback-функции: одну для отмены и другую для подтверждения. Компонент должен быть всегда поверх остальных элементов на экране, включая элементы "popover" и `<dialog/>`.

## Пример использования

```jsx
{showCreationModal && (
    <GenericModal
        title={'Новый проект'}
        subtitle={'Введите название и часовой пояс'}
        onSubmit={handleCreateProject}
        onCancel={() => setShowCreationModal(false)}
    >
        {/* Это тело компонента, сюда другие разработчики могут передать что угодно. */}
        <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <UniTextarea
                setInternalValue={setInternalValue}
                value={internalValue}
                placeholder="Название проекта*"
                onChange={handleChangeText}
                className={textareaError}
                error={textareaError}
            />
            <MultiSelect
                value={selectValue}
                options={searchOptions}
                handleChange={handleChangeSelector}
                isMulti={false}
                style={styleMulti}
                placeholder={'Выбрать часовой пояс'}
            />
        </div>
        {/* Конец children */}
    </GenericModal>
)}
```

## Примерный дизайн компонента

Можете ориентироваться на него, но точь-точь попасть в дизайн не нужно.
<img width="654" height="540" alt="image" src="https://github.com/user-attachments/assets/0f86303e-38b8-4079-b5ba-d7fe2f05ef55" />

## Проверка

Для проверки, пожалуйста, отправьте ссылку на GitHub репозиторий с кодом компонента.

## Удачи
