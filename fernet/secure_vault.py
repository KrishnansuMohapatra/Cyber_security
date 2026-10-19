from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

KEY_FILE = Path("secret.key")


def load_or_generate_key():
    """Load the existing key or generate it if it doesn't exist."""

    if KEY_FILE.exists():
        key = KEY_FILE.read_bytes()
        console.print("🔑 [green]Existing key loaded.[/green]")
    else:
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        console.print("🔑 [yellow]New key generated and saved.[/yellow]")

    return Fernet(key)


def encrypt_file(filename, cipher):
    """Encrypt a file and save it with .encrypted extension."""

    input_file = Path(filename)

    if not input_file.exists():
        console.print("❌ [bold red]File not found.[/bold red]")
        return

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    output_file = Path(str(input_file) + ".encrypted")

    with open(output_file, "wb") as file:
        file.write(encrypted)

    console.print("🔐 [bold green]File encrypted successfully.[/bold green]")
    console.print(f"📁 [cyan]Saved as: {output_file}[/cyan]")


def decrypt_file(filename, cipher):
    """Decrypt an encrypted file."""

    input_file = Path(filename)

    if not input_file.exists():
        console.print("❌ [bold red]Encrypted file not found.[/bold red]")
        return

    with open(input_file, "rb") as file:
        encrypted = file.read()

    try:
        decrypted = cipher.decrypt(encrypted)

    except InvalidToken:
        console.print("❌ [bold red]Decryption failed.[/bold red]")
        console.print("[red]The key may be incorrect or the file may have been modified.[/red]")
        return

    if str(input_file).endswith(".encrypted"):
        output_file = Path(str(input_file)[:-10])
    else:
        output_file = Path(str(input_file) + ".decrypted")

    with open(output_file, "wb") as file:
        file.write(decrypted)

    console.print("🔓 [bold green]File decrypted successfully.[/bold green]")
    console.print(f"📁 [cyan]Saved as: {output_file}[/cyan]")


def show_menu():
    menu_text = Text()
    menu_text.append("1. ", style="bold cyan")
    menu_text.append("Encrypt file\n")
    menu_text.append("2. ", style="bold cyan")
    menu_text.append("Decrypt file\n")
    menu_text.append("3. ", style="bold cyan")
    menu_text.append("Exit")

    console.print(
        Panel(
            menu_text,
            title="[bold blue]🔐 SECURE VAULT[/bold blue]",
            border_style="magenta",
            expand=False,
        )
    )


def main():
    cipher = load_or_generate_key()

    while True:
        console.print()
        show_menu()

        choice = Prompt.ask(
            "[yellow]Choose an option[/yellow]",
            choices=["1", "2", "3"],
            show_choices=False,
        )

        if choice == "1":
            filename = Prompt.ask("[yellow]Enter file to encrypt[/yellow]")
            encrypt_file(filename, cipher)

        elif choice == "2":
            filename = Prompt.ask("[yellow]Enter encrypted file[/yellow]")
            decrypt_file(filename, cipher)

        elif choice == "3":
            console.print("[magenta]👋 Goodbye![/magenta]")
            break


if __name__ == "__main__":
    # ── Demo: non-interactive round trip so you can see it work end-to-end ──
    console.print(Panel("[bold]Running demo mode[/bold]", border_style="green"))

    cipher = load_or_generate_key()

    demo_file = Path("demo.txt")
    demo_file.write_text("hello from the secure vault demo")
    console.print(f"📝 [cyan]Created demo file: {demo_file}[/cyan]")

    encrypt_file(str(demo_file), cipher)
    decrypt_file(str(demo_file) + ".encrypted", cipher)

    console.print(Panel("[bold]Demo complete — launching interactive menu[/bold]", border_style="green"))

    main()