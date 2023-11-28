import {Layout} from "antd"

const {Footer} = Layout

export default function FooterWarp() {
    return (
        <Footer className="bg-gray-800 text-white text-center"
        >
            5piderMan ©{new Date().getUTCFullYear()} Created by 5piderMan Team
        </Footer>
    );
}
