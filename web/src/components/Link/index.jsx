export default function Link(prop) {
    return <a href={prop.href}>
        {prop.children}
    </a>
}