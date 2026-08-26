# Steam & Ember

## A quiet workspace for Markdown and Python

### Espresso after sunset

#### Crema in daylight

##### A softer fifth level

###### The quietest heading

Обычный текст остаётся спокойным. **Важная мысль выглядит теплее**, а *небольшое
уточнение — тише*. Ссылка ведёт к [документации Sublime Text](https://www.sublimetext.com/docs/).

> Хорошая тема не перетягивает внимание на себя.
> Она помогает дольше оставаться в тексте.

- тёплый коричневый фон;
- оранжевый акцент;
- разные, но спокойные цвета синтаксиса;
- [x] Espresso готов к первому тесту;
- [ ] проверить Crema на реальном дисплее.

`inline_code()` получает отдельный кофейный фон.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coffee:
    name: str
    temperature: int = 67

    def serve(self, with_sugar: bool = False) -> str:
        suffix = " with sugar" if with_sugar else ""
        return f"{self.name} at {self.temperature}°C{suffix}"
```

> [!NOTE]
> Заметка использует холодный приглушённый оттенок.

> [!TIP]
> Совет получает спокойный шалфейный цвет.

> [!WARNING]
> Предупреждение заметно, но не кричит.

---

Финальная цель — интерфейс, который ощущается как чашка флэт-уайта рядом с
рабочим блокнотом.
